import os
import time

import requests


def main():
    default_frontend_to_watch = ["main_frontend", "admin_panel_frontend"]
    frontend_to_watch_env = os.getenv("FRONTEND_TO_WATCH")
    base_stats_path = os.getenv("BASE_STATS_PATH", "/front/webpack-stats").strip() or "/front/webpack-stats"
    watch_port = os.getenv("WATCH_PORT", "8000").strip() or "8000"
    trigger_reload_url = f"http://localhost:{watch_port}/api/auto-reload/trigger-reload"
    frontend_to_watch = (
        [name.strip() for name in frontend_to_watch_env.split(",") if name.strip()]
        if frontend_to_watch_env
        else default_frontend_to_watch
    ) or default_frontend_to_watch

    def try_get_timestamp(name):
        try:
            return os.path.getmtime(f"{base_stats_path}/{name}/webpack-stats.json")
        except FileNotFoundError:
            return None

    last_frontend_timestamps = {name: try_get_timestamp(name) for name in frontend_to_watch}

    try:
        time.sleep(4.0)
        while True:
            time.sleep(1.0)
            main_frontend = frontend_to_watch[0]
            os.path.getmtime(f"{base_stats_path}/{main_frontend}/webpack-stats.json")

            changed = False
            new_frontend_timestamps = {name: try_get_timestamp(name) for name in frontend_to_watch}

            for key in new_frontend_timestamps:
                if new_frontend_timestamps[key] != last_frontend_timestamps[key]:
                    print(f"Detected change in {key}")
                    last_frontend_timestamps[key] = new_frontend_timestamps[key]
                    changed = True

            if changed:
                try:
                    requests.get(trigger_reload_url)
                except Exception as e:
                    print(f"Failed to trigger reload: {e}")

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

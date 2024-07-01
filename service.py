import datetime
import sys
import xbmc
import xbmcgui
import xbmcaddon


def hourly_chime(demo=False):

    monitor = xbmc.Monitor()
    addon = xbmcaddon.Addon()

    if demo:
        # Demo mode
        nowtime = datetime.datetime.now().strftime("%H:%M")
        enalbe_sound = addon.getSettingBool("enalbe_sound")
        notification_duration = addon.getSettingInt("notification_duration") * 1000

        total_time = 707
        watched_time = 305
        watched_percent = str(round(watched_time / total_time * 100)) + "%"

        default_text = f"{addon.getLocalizedString(30030)}{watched_percent}"

        title = addon.getSettingString("customized_notification_title")
        text = addon.getSettingString("customized_notification_text")

        if addon.getSettingString("customized_notification_title"):
            notification_title = eval(f"f'{title}'")
            # notification_title = addon.getSettingString("customized_notification_title").format(total_time=total_time, watched_time=watched_time, watched_percent=watched_percent, nowtime=nowtime)
        else:
            notification_title = nowtime
        if addon.getSettingString("customized_notification_text"):
            notification_text = eval(f"f'{text}'")
            # notification_text = addon.getSettingString("customized_notification_text").format(total_time=total_time, watched_time=watched_time, watched_percent=watched_percent, nowtime=nowtime)
        else:
            notification_text = default_text

        xbmcgui.Dialog().notification(notification_title, notification_text, xbmcgui.NOTIFICATION_INFO, notification_duration, enalbe_sound)
        return

    is_first_time = True
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break

        # Don't run if the DPMS or screensaver is active
        if monitor.onDPMSActivated() or monitor.onScreensaverActivated():
            continue

        # Don't run if the player is not playing
        if xbmc.Player().isPlaying():
            nowtime = datetime.datetime.now().strftime("%H:%M")
            # Get the settings
            is_half_hour = addon.getSettingBool("is_half_hour")
            enalbe_sound = addon.getSettingBool("enalbe_sound")
            notification_duration = addon.getSettingInt("notification_duration") * 1000
            # Check if the current time is a half hour
            if nowtime[-2:] == "00":
                if not is_first_time:
                    continue
            elif is_half_hour and nowtime[-2:] == "30":
                if not is_first_time:
                    continue
            else:
                is_first_time = True
                continue

            # Get the current time and watch progress
            try:
                total_time = xbmc.Player().getTotalTime()
                watched_time = xbmc.Player().getTime()
                watched_percent = str(round(watched_time / total_time * 100)) + "%"

                default_text = f"{addon.getLocalizedString(30030)}{watched_percent}"

                title = addon.getSettingString("customized_notification_title")
                text = addon.getSettingString("customized_notification_text")

                if addon.getSettingString("customized_notification_title"):
                    notification_title = eval(f"f'{title}'")
                    # notification_title = addon.getSettingString("customized_notification_title").format(total_time=total_time, watched_time=watched_time, watched_percent=watched_percent, nowtime=nowtime)
                else:
                    notification_title = nowtime
                if addon.getSettingString("customized_notification_text"):
                    notification_text = eval(f"f'{text}'")
                    # notification_text = addon.getSettingString("customized_notification_text").format(total_time=total_time, watched_time=watched_time, watched_percent=watched_percent, nowtime=nowtime)
                else:
                    notification_text = default_text

            except:
                notification_title = ""
                notification_text = ""

            # Show a notification
            is_first_time = False
            xbmcgui.Dialog().notification(
                notification_title, notification_text, xbmcgui.NOTIFICATION_INFO, notification_duration, enalbe_sound
            )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        hourly_chime(demo=True)
    else:
        hourly_chime()

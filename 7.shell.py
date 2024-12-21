# import ctypes
# from ctypes import wintypes

# # Load user32.dll functions
# user32 = ctypes.windll.user32

# # Define function prototype for EnumWindowsProc
# EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)


# def show(pid, showcode=5):
#     """Restore the main window of a process given its PID."""

#     @EnumWindowsProc
#     def callback(hwnd, lParam):
#         # Get the PID associated with the hwnd
#         lpdwProcessId = wintypes.DWORD()
#         user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdwProcessId))
#         # print(
#         #     lpdwProcessId,
#         #     lpdwProcessId.value,
#         #     # lParam,
#         #     type(lpdwProcessId.value),
#         #     type(lParam),
#         #     end=" ",
#         # )
#         # Compare the process ID
#         if lpdwProcessId.value == lParam:
#             namelen = user32.GetWindowTextLengthW(hwnd)
#             namebuffer = ctypes.create_unicode_buffer( + 1)
#             user32.GetWindowTextW(hwnd, namebuffer, namelen + 1)
#             window_name = namebuffer.value
#             print(f"Restoring window for PID {lpdwProcessId.value}: {window_name} HWND {hwnd} code {showcode}")
#             user32.ShowWindow(hwnd, showcode)
#             return False # we done
#         return True  # Continue enumeration

#     # Pass the PID as an LPARAM (64-bit on 64-bit systems)
#     user32.EnumWindows(callback, wintypes.LPARAM(pid))


# # Example usage: restore PID 3980

# def pidforeground() -> int:
#     h = user32.GetForegroundWindow()
#     pid = wintypes.DWORD()
#     user32.GetWindowThreadProcessId(h, ctypes.byref(pid))
#     return pid.value
# # why do you do this 
# show(pidforeground(), 2) 


import subprocess


with subprocess.Popen([
    "powershell.exe",
    "-NoExit",  # Don't exit after running commands
    "-NoLogo",  # Skip the copyright banner if you want
    "-ExecutionPolicy", "Bypass",  # Ensure scripts can run
    "-Command", "$Host.UI.RawUI.WindowTitle = 'power shell'"  # Optional: custom window title
]) as process:
    process.wait()
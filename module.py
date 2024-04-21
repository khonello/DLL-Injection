import win32process
import win32api
import win32con
import win32event
import os
import psutil


dll_path = r"path\to\library.dll"
dll_stat = os.stat(dll_path)

h_kernel32 = win32api.GetModuleHandle("kernel32.dll")
h_loadlib = win32api.GetProcAddress(h_kernel32, "LoadLibraryA")

for process in psutil.process_iter(["name", "pid"]):
    if process.name().startswith("console"):

        target_process_handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, process.pid)
        allocated_memory = win32process.VirtualAllocEx(target_process_handle, 0, dll_stat.st_size, win32con.MEM_RESERVE | win32con.MEM_COMMIT, win32con.PAGE_READWRITE)

        win32process.WriteProcessMemory(target_process_handle, allocated_memory, dll_path)

        thread_handle, thread_id = win32process.CreateRemoteThread(target_process_handle, None, 0, h_loadlib, allocated_memory, win32con.CREATE_SUSPENDED)

        win32process.ResumeThread(thread_handle)
        win32event.WaitForSingleObject(thread_handle, -1)

        win32process.VirtualFreeEx(target_process_handle, allocated_memory, 0, win32con.MEM_FREE)

        win32api.CloseHandle(thread_handle)
        win32api.CloseHandle(target_process_handle)
        break

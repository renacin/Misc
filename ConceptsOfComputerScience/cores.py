import multiprocessing as mp
import platform

platform_ = platform.processor()
cores_ = mp.cpu_count()
print("Platform: {},\nCores: {}".format(platform_, cores_))

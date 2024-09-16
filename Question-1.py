import logging
from mpi4py import MPI

# Logger for potential output saving purposes.
logger = logging.getLogger('advanced_logger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('Question-1.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# MPI Standard initialization. Sets comm_world along with gathering the rank of the root process and size of total
# processes.
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# If root process begin sequence by sending task to next processor.
if rank == 0:
    print(f"Hello from Processor {rank}")
    logger.info(f"Hello from Processor {rank}")
    comm.send(None, dest=rank + 1)

# After root process, recieve the task by the ith + 1 rank processor. If the processor isn't last in the list continue
# to send the process down the chain.
else:
    comm.recv(source=rank - 1)

    print(f"Hello from Processor {rank}")
    logger.info(f"Hello from Processor {rank}")

    if rank < size - 1:
        comm.send(None, dest=rank + 1)

    if rank == (size - 1):
        MPI.Finalize()
        print("Processed Finalized")
        logger.info("Processed Finalized\n")

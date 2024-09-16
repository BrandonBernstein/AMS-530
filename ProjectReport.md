# AMS 530 Problem 1.1 Report

The order in which processor threads complete their task after the initial activation latency can be random. The same computer running a core with 10 threads may have processors 3, 2, 1, 4, ..., 10 activate in order during an initial script run while obtaining a completely different sequence on future iterations.

To rectify this, `Question-1.py` contains code to check the processor's order and output according to its rank. The following pseudo-code is applied:

```pseudo
Check the rank of the processor with Get_Rank()
  if rank == 0:
      Send a null value to rank 1 using the send method
  else:
      Receive null value from processor (rank-1) using the recv method
      Print processor rank

      if rank == size - 1:
          Print processor rank and finalize the script

      else:
          Send null to processor (rank+1)


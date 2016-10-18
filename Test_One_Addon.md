Test-1 Helper
=======================================================
Define the following and give examples of each:
-------------------------------------------------------
### 1. Multi-tasking:
Multitasking, in an operating system, is allowing a user to perform more than one computer task (such as the operation of an application program) at a time. In simpler words Multitasking,is to expand memory to hold three, four, or more
tasks and switch among all of them. It is the central theme of modern operating systems  when multiple tasks share a common processing resource
(e.g., CPU and Memory).The operating system will keep track of all these tasks and switch among them without losing information.
### Example: 
 Microsoft Windows 2000, IBM's OS/390, and Linux are examples of operating systems that can do multitasking (almost all of today's operating systems can). When you open your Web browser and then open Word at the same time, you are causing the operating system to do multitasking.

### 2. Multi-programming: 
In multiprogramming, there are one or more programs loaded in main memory which are ready to execute. Only one program at a time is able to get the CPU for executing its instructions (i.e., there is at most one process running on the system) while all the others are waiting their turn.
Here, there can be no true simultaneous execution of different programs, but to the user it appears that all programs are executing at the same time.
### Example:
A computer running Word,PDF, and Chrome browser at a time, is an example of multiprogramming.
 
### 3. Multi-processing:
Multiprocessing is the ability of an operating system to execute multiple processes at the same time. It refers to the hardware (i.e., the CPU units)
rather than the software (i.e., running processes). If the hardware provides more than one processor, then that is multiprocessing.
### Example:
A prime example of this is the Pool object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism).

### 4. Multi-threaded:
Multithreading is the ability of a central processing unit (CPU) or a single core in a multi-core processor to execute multiple processes or threads concurrently, appropriately supported by the operating system. In other words, Multithreading is the ability of an operating system to execute the different parts of a program called threads at the same time. Threads are the light wait processes which are independent part of a process or program. In multithreading system, more than one threads are executed parallely on a single CPU.
### Real Life Example:
There will be a Team leader in a team, who assigns individual tasks for the team members and he have control on each task status, which is nothing but a thread. So at any given time, the team as a whole is working on multiple tasks. But at the same time, the team lead knowing the status report of all tasks and maintaining a report of all at one place. There may/ may not have dependencies on each other's tasks. They all need to be completed parallel.

Review Questions From Chapters 3
==============================================================
### 1. What is an instruction trace?
We can characterize the behavior of a process by listing the sequence of instructions that execute for that process.
Such a listing is referred to as a trace of the process. This is done by showing how the traces of various processes are interleaved.

### 2. What common events lead to the creation of a process?
Four common events lead to the creation of process. They are:
- New batch job
- Interactive log-on
- Created by OS to provide a service
- Spawned by existing process

### 3. What does it mean to preempt a process?
Process preemption is a situation where a process will be interrupted so that the other processes which are waiting in the queue will be 
executed after unit time. It is executing and could continue to execute, but is preempted so that another process can be executed.
A process will be executed for a certain amount of time to which it is set.
Each process will stop after the unit time and if it is not accomplished it will wait in the queue for it's turn.


### 4. What is swapping and what is its purpose?
Swapping is a technique for memory/process management used by the operating system for increasing the utilization of the resources and to 
accommodate more processes. During the process of swapping part of the process or all of the process will be moved from main memory to disk.
This will result in forming of a queue of temporarily suspended process. The execution continues with the newly arrived process.

### 5. Why does Figure 3.9b have two blocked states?
To accommodate the two different combinations we need two blocked states and two suspended states. They are: 
- Whether a process has been swapped out of main memory (suspended or not). 
- To know whether a process is waiting on an event (blocked or not).

### 6. List four characteristics of a suspended process.
- The process is not immediately available for execution.
- The process may or may not be waiting on an event. If it is, this blocked condition is independent of the suspend condition,
and occurrence of the blocking event does not enable the process to be executed.
- The process was placed in a suspended state by an agent; either itself, a parent process, or the operating system,
for the purpose of preventing its execution.
- The process may not be removed from this state until the agent explicitly orders the removal.

### 7. List three general categories of information in a process control block.
- Processor state information.
- Process control information.
- Process identification.

### 8. Why are two modes (user and kernel) needed?
The less-privileged mode is often referred to as the user mode, the more-privileged mode is referred
to as the system mode, control mode, or kernel mode. It is necessary to protect the OS and key operating system tables,
such as process control blocks, from interference by user programs. In the kernel mode, 
the software has complete control of the processor and all its instructions, registers, and memory. This level of control is not
necessary and for safety is not desirable for user programs. User mode has restrictions on the instructions that can be executed and the
memory areas that can be accessed.

### 9. What is the difference between an interrupt and a trap?
An interrupt is independent of the currently running process and is caused due to some sort of event that is external event like
completion of I/O operation. A trap is an error or an exception condition generated within the currently running
process like illegal file access attempt.

### 10. Give three examples of an interrupt.
- I/O interrupt
- Memory fault
- Clock interrupt


### 11. What is the difference between a mode switch and a process switch?
A mode switch may occur without changing the state of the process that is currently in the Running state.
A process switch involves taking the currently executing process out of the Running state in favor of another process 
which involves saving more state information.


#References:
- Google.com
- http://www.thecrazyprogrammer.com/2014/12/difference-between-multiprogramming-multitasking-multiprocessing-multithreading.html
- https://gabrieletolomei.wordpress.com/miscellanea/operating-systems/multiprogramming-multiprocessing-multitasking-multithreading/
- Operating Systems Internals and Design Principles Seventh Edition by William Stallings













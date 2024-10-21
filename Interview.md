# Amazon 16 leadership principles (behavior)  
https://www.amazon.jobs/content/en/our-workplace/leadership-principles



# 什么是thread，process，他们的关系？

A thread and a process are both fundamental concepts in computer programming for handling concurrent tasks. They help improve the efficiency and execution speed of programs, but they differ in nature and how they are used.

## 1. Process
Definition: A process is an instance of a program running on a computer. Each process has its own memory space, data, code, and resources.
Characteristics:
Independence: A process is an independent unit, and the operating system allocates separate memory for each process. One process cannot directly access another process's memory unless they communicate through Inter-Process Communication (IPC).
Resource management: A process has its own file descriptors, stack, registers, and address space. The operating system manages resources for the process.
High overhead: Creating, destroying, or switching between processes is resource-intensive because it requires switching context (e.g., saving and restoring CPU registers, changing memory, etc.).
Example: A web browser, text editor, or any application running on your system is a process.

## 2. Thread
Definition: A thread is a unit of execution within a process, often referred to as a "lightweight process." A process can have multiple threads, and these threads share the process's resources.
Characteristics:
Shared memory: All threads in a process share the same memory space (like the heap and global variables), making communication between threads easier and faster compared to communication between processes.
Independent execution: Each thread has its own program counter (PC), registers, and stack, so it can run independently.
Lower overhead: Threads are less resource-intensive to create and switch between because they don’t need separate memory spaces.
Concurrent execution: Multiple threads can run concurrently within the same process. For example, in a browser process, one thread might handle user input while another loads a webpage.

## 3. Relationship between Process and Thread
Threads belong to processes: A process can contain multiple threads, and threads cannot exist independently of a process. Each process has at least one main thread (the one that starts the process).

Shared vs. isolated memory: Threads within the same process share memory and global variables, while processes are isolated from each other and have their own memory. This makes communication between threads faster, but it also introduces challenges like thread safety (e.g., race conditions when multiple threads try to access the same resource).

Concurrency model: Processes are suited for tasks that need strong isolation because each process has its own resources and memory. Threads are better for tasks that are part of the same overall job because they share resources.

## 4. Summary
Process: An independent instance of a running program, with separate memory and resources.
Thread: A lightweight unit of execution within a process that shares resources with other threads in the same process.
Relationship: A thread is dependent on a process, and the process acts as a container for threads. Threads are more lightweight and suited for concurrent execution, while processes are better for tasks that require strict separation and isolation.
In short, both processes and threads enable concurrency, but they differ in terms of how they share resources and the overhead involved in managing them.


# Jacobian matrix, hessian matrix
梯度向量Jacobian矩阵的一个特例；
## Jacobian matrix

Used in neural networks and multi-output models to compute the gradient of the output with respect to the input.
Helps propagate errors in backpropagation and update weights.
Essential for understanding the sensitivity of model outputs to changes in inputs.


## hessian matrix

The Jacobian matrix captures the first-order partial derivatives, showing how the model's output changes with respect to the input. The Hessian matrix contains second-order derivatives, describing the curvature of the loss function and helping in optimization. Both are essential in machine learning for understanding gradients and improving convergence in optimization algorithms.


hessian 是梯度向量 g(x) 对自变量x 的Jacobian 矩阵


# cap theorem

The CAP theorem (Consistency, Availability, Partition Tolerance) explains the trade-offs in distributed systems:

Consistency: Every read reflects the most recent write.
Availability: Every request gets a response, even if it's not the most up-to-date.
Partition Tolerance: The system remains operational despite network failures or partitions.
The theorem states that a distributed system can only guarantee two of the three at any given time, forcing designers to make trade-offs based on the system's needs.


# Mutex and semaphore 解释


Mutex and Semaphore are synchronization mechanisms used to manage access to shared resources in concurrent programming.

Mutex (Mutual Exclusion) allows only one thread to access a critical section at a time. Once a thread locks the mutex, no other thread can access the resource until the mutex is unlocked by the owning thread.

Semaphore is a signaling mechanism that controls access to a resource by maintaining a counter. It allows multiple threads to access a resource up to a specified limit (in the case of a counting semaphore) or enforces mutual exclusion (in the case of a binary semaphore).

In short, a mutex ensures exclusive access to a single resource, while a semaphore can allow multiple accesses based on its count.

# Unix pipe 是什么？

A Unix pipe is a mechanism that allows the output of one process to be used as the input for another process, enabling communication between processes. It is represented by the | symbol and helps connect commands so that the data flows seamlessly from one to the next.


# Byzantine generals problem

The Byzantine Generals Problem is a computer science challenge that describes the difficulty of reaching consensus in a distributed network, such as a machine learning system: 
Problem
Multiple generals, each leading a division of an army, must agree on whether to attack or retreat to conquer a city. Some generals may be traitors who try to sabotage the mission by giving misleading information. 
Solution
The challenge is to find a protocol that allows the loyal generals to reach a consensus, even in the presence of traitors. The solution requires an algorithm that ensures traitors can't tamper with messages. 
Applications
The Byzantine Generals Problem is relevant to computer networks, where it's important to ensure that computers can reach a consensus even when some of them are faulty or malicious. 

# 强化学习，什么是on policy off policy, TRPO ppo 有什么区别联系，优劣


In reinforcement learning, on-policy methods (e.g., PPO) learn from the current policy, while off-policy methods (e.g., DQN) learn from data generated by a different policy, allowing for experience reuse.

TRPO (Trust Region Policy Optimization) ensures stable updates by limiting how much the policy can change, but it's complex and computationally expensive. PPO (Proximal Policy Optimization) simplifies TRPO by using a clipping mechanism to control updates, making it more efficient and widely used.

In interviews, you can explain that PPO is favored for its simplicity and efficiency, while TRPO is used when stability is critical.

# transformer mask加在什么地方？
In a Transformer model, masks are used in two key places to control the flow of information during training and inference:

Padding Mask: Applied in the encoder and decoder to prevent the model from attending to padding tokens. Padding tokens are used to make all input sequences the same length, and the mask ensures these tokens don't affect the learning process. The padding mask is typically applied to the attention mechanism to block attention to these positions.

Look-Ahead Mask (or Causal Mask): Applied in the decoder during training to prevent the model from looking ahead at future tokens when generating output. This ensures the model can only attend to previous tokens and the current token, preserving the autoregressive nature of the model.

These masks are critical for ensuring that the model behaves correctly when dealing with variable-length sequences and during autoregressive generation tasks like text generation.
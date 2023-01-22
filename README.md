# DIPC Project

## Distributed Inter-Process Communication Project

---

## Description

Aim of this project is to design and implement 4 processes with communication in order to transfer the data.

Project was developed with OS Linux (Debian distro) with preconfigured *Apache2* and *nginx*.

---

## Communication Mechanisms

### 1. SOAP

### 2. Socket / TCP

### 3. XML-RPC

---

## Processes Roles

### Process I

#### **Technology:** *Perl*

Process retrieves data from the *standard input stream* and passes it to the next process using **the first communication mechanism**.

### Process II

#### **Technology:** *PHP*

Process receives data from the first process, count data bytes and passes it to the standard error stream. Moreover, process passes data to the next process using **the second communication mechanism**.

### Process III

#### **Technology:** *Python*

Process receives data from the second process, count data bytes and passes it to the standard error stream. Next, process passes data to the last process using **the third communication mechanism**.

### Process IV

#### **Technology:** *Java*

Process receives data from the previous process and passes it to the standard output stream.

# Mission 07 — How Computers Communicate

## 1. Task / Objective

The objective of this mission is to understand basic computer networking concepts, explore network connectivity, perform DNS lookups and understand the sequence of events involved in opening a website.

In this mission, I used macOS Terminal to perform practical network tests and studied how computers communicate over the Internet.

## 2. Work Completed

### Task 7.1 — Explain Network Concepts

A computer network connects multiple devices, allowing them to exchange information and share resources.

| Concept | Explanation | Example |
|---|---|---|
| LAN (Local Area Network) | A network covering a small geographical area. | Home Wi-Fi network |
| MAN (Metropolitan Area Network) | A network covering a city or metropolitan area. | City-wide university network |
| WAN (Wide Area Network) | A network connecting smaller networks across large geographical areas. | The Internet |
| DNS (Domain Name System) | Translates domain names into IP addresses. | Resolving example.com |
| Router | Connects different networks and forwards data between them. | Home Wi-Fi router |
| Protocol | A set of rules that devices follow to communicate. | HTTP, HTTPS and TCP |
| Packet Switching | Divides data into smaller packets for transmission across a network. | Transferring data over the Internet |
| Client-Server | A communication model in which a client requests a service and a server provides it. | A browser requesting a webpage |

### Task 7.2 — Observe Network Information

I used macOS Terminal to perform a connectivity test and a DNS lookup.

**1. Connectivity Test Using Ping**

**Command Used**

```bash
ping -c 4 example.com
```

**Purpose**

The `ping` command checks whether a destination is reachable over a network. It also provides information about round-trip response times and packet loss.

The `-c 4` option limits the test to four requests.

**Individual Response Times**

| Packet | Response Time |
|---|---:|
| Packet 1 | 6.631 ms |
| Packet 2 | 5.014 ms |
| Packet 3 | 4.630 ms |
| Packet 4 | 8.657 ms |

**My Observations**

| Information | Result |
|---|---|
| Domain Tested | example.com |
| Destination IP Address | 104.20.23.154 |
| Packets Transmitted | 4 |
| Packets Received | 4 |
| Packet Loss | 0.0% |
| Minimum Response Time | 4.630 ms |
| Average Response Time | 6.233 ms |
| Maximum Response Time | 8.657 ms |
| Standard Deviation | 1.588 ms |

**Selected Terminal Output**

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.630/6.233/8.657/1.588 ms
```

**Observation**

All four packets received successful responses, resulting in zero packet loss.

The average round-trip response time was 6.233 milliseconds, indicating a responsive network connection to the destination during the test.

The response times varied slightly between individual requests.

**2. DNS Lookup**

**Command Used**

```bash
nslookup example.com
```

**Purpose**

The `nslookup` command retrieves DNS information, including IP addresses associated with a domain name.

**My Observations**

| Information | Result |
|---|---|
| Domain Name | example.com |
| DNS Lookup Status | Successful |
| First Resolved IP Address | 104.20.23.154 |
| Second Resolved IP Address | 172.66.147.243 |
| Response Type | Non-authoritative answer |

**Selected Terminal Output**

```text
Non-authoritative answer:

Name:    example.com
Address: 104.20.23.154

Name:    example.com
Address: 172.66.147.243
```

DNS resolver details and personal system identifiers have been excluded from the documentation.

**Observation**

The DNS lookup successfully returned two IP addresses associated with example.com.

A non-authoritative answer means that the response was provided by a DNS resolver rather than directly by the authoritative DNS server for the domain.

**3. Answers to the Questions**

**Q1. What does a connectivity test help you check?**

A connectivity test helps determine whether a computer can communicate with another device or server over a network. It also provides information about packet loss and round-trip response times.

**Q2. What information does a DNS lookup display?**

A DNS lookup displays information associated with a domain name, including its resolved IP addresses and details about the DNS server that provided the response.

**Q3. Describe the role of DNS when you enter a website name in a browser.**

DNS translates a human-readable domain name into an IP address. This allows the browser to locate the network destination and communicate with the server hosting the website.

### Task 7.3 — What Happens When You Open a Website?

The following steps explain the communication process that takes place when a user opens a website.

1. **Entering the URL:** The user enters a website address into a browser. The browser acts as the client.

2. **DNS Resolution:** DNS helps the browser obtain an IP address associated with the domain name.

3. **Network Communication:** Data travels through routers and other networking devices towards the destination server.

4. **Connection Establishment:** The browser establishes a connection using appropriate networking protocols. HTTPS uses encryption to protect communication.

5. **Sending the Request:** The browser sends an HTTP or HTTPS request asking the server for the required webpage.

6. **Receiving the Response:** The server processes the request and returns the requested resources, such as HTML, CSS, JavaScript and images.

7. **Displaying the Website:** The browser processes the received resources and renders the webpage on the user's screen.

This process demonstrates how DNS, routers, communication protocols, clients and servers work together to provide access to websites.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `ping -c 4 example.com` | Performs a connectivity test using four requests. |
| `ping` | Checks destination reachability and measures round-trip response times. |
| `nslookup example.com` | Retrieves IP addresses associated with a domain name. |
| macOS Terminal (Zsh) | Used to execute networking commands and observe their outputs. |
| DNS | Used to resolve domain names into IP addresses. |

## 4. My Understanding

Through this mission, I understood how computers communicate and exchange information over networks.

I learned the following concepts:

1. LAN, MAN and WAN are different types of networks classified according to their geographical coverage.
2. DNS allows users to access websites using domain names instead of remembering numerical IP addresses.
3. Routers forward data between different networks.
4. Communication protocols provide standard rules for exchanging information.
5. Packet switching allows data to be transmitted in smaller units called packets.
6. The client-server model explains how clients request information and servers provide responses.
7. The `ping` command helps test network connectivity, response times and packet loss.
8. The `nslookup` command helps retrieve DNS information associated with a domain name.
9. Opening a website involves several networking operations working together.

I also understood that successful DNS resolution and successful network connectivity are related but serve different purposes.

## 5. Difficulties Faced

**Difficulty 1: Understanding Network Test Results**

Initially, interpreting the different response times and packet-loss statistics displayed by the `ping` command required additional understanding.

**Difficulty 2: Understanding DNS Lookup**

Understanding why a single domain name could resolve to multiple IP addresses required further explanation.

**Difficulty 3: Understanding Website Communication**

It was important to understand how DNS, routers, servers and protocols work together when accessing a website.

## 6. How I Resolved Them

**Solution 1:**

I examined the individual ping responses and the final statistics to understand minimum, average and maximum round-trip response times.

I understood that zero packet loss means that all four requests received successful responses during the test.

**Solution 2:**

I studied the output of the `nslookup` command and understood that a domain name can be associated with multiple IP addresses.

I also learned the meaning of a non-authoritative DNS response.

**Solution 3:**

I divided the website-loading process into seven steps, starting from entering a URL and ending with the browser displaying the webpage.

This helped me understand the role of each networking component.

## 7. Evidence / Files

The following files and observations are associated with this mission:

- `mission-07-networking/README.md` — Documentation of Tasks 7.1 to 7.3.
- Network concepts table explaining LAN, MAN, WAN, DNS, routers and communication protocols.
- Connectivity test results obtained using `ping -c 4 example.com`.
- Four successful ping responses with 0.0% packet loss.
- Average round-trip response time of 6.233 ms.
- DNS lookup results containing two resolved IP addresses.
- Seven-step explanation of how a website opens in a browser.

All practical observations are based on the Terminal output obtained during this mission.

Personal system identifiers and unnecessary network configuration details have been excluded to maintain privacy.

## 8. Commit Details

**Commit Message:**

```text
Explain networking concepts and website communication
```

The mission documentation is to be staged, committed and pushed to the main branch of the GitHub repository.
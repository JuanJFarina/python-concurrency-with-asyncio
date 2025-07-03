### TCP Client–Server Lifecycle

- A server begins by creating a **“listening” socket** and telling the OS, “I’m
  ready to accept incoming connections on this port,” at which point that socket
  sits quietly in a LISTEN state.
- A client likewise creates its own socket and **reaches out to the server’s
  address and port**, triggering the three‑way handshake:
  - The client sends SYN (“Hello, here’s my sequence number”)
  - The server replies SYN+ACK (“I acknowledge you, here’s mine”)
  - The client finishes with ACK (“Got it—let’s chat!”).
- Once the handshake completes, the OS pairs up the two sockets and the
  server’s original listening socket automatically **“accepts” the connection**
- Behind the scenes spawns a second, **dedicated server‑side socket just for
  that client**, while the original stays free to listen for others.

### Data Exchange & Teardown

With that dedicated socket pair in place, client and server enjoy a 
**full‑duplex channel**—each can send and receive at will, and multiple clients 
can connect simultaneously without interference. When either side is done, it 
initiates a graceful shutdown (the TCP FIN/ACK exchange), both ends acknowledge 
the closure, and the sockets are released.

Think of it like a switchboard operator: the listening socket is the operator’s
headset always on standby, and each incoming call gets its own private line for
the conversation, leaving the headset free to handle more calls.

### Listening Socket vs. Per‑Connection Socket

A server’s listening socket is created and placed into LISTEN mode so it can
queue up incoming “knock‑knock” requests—but it cannot send or receive
application data itself. When a client calls connect, the OS performs the TCP
handshake on the listening socket’s behalf, then hands off the established
connection to a newly spawned per‑client socket. That dedicated socket pair is
the one your application uses to both send and receive stream data in
full‑duplex, and you can have as many of these live at once as you have clients.

### How a Per‑Connection Socket Knows Its Peer

Each per‑client socket internally carries the full TCP four‑tuple—(local IP,
local port, remote IP, remote port)—so the OS always knows exactly which client
endpoint it’s talking to. When you write to that socket, your bytes are
automatically packaged and routed to the correct remote address, and incoming
packets from that same address are demultiplexed back into your program’s read
calls.

### How a Typical Web Server Works Under the Hood

- When your server starts (e.g. on port 80 or 443), it creates **one** listening socket bound to that port. This socket’s sole responsibility is to wait for incoming **TCP connection requests**—it does **not** send or receive actual HTTP data.
- Each time a client connects, the OS completes the TCP three‑way handshake on the listening socket’s behalf, then hands your application a **new, dedicated socket** (via `accept()`). You end up with:
  - **1 listening socket** (still in LISTEN state, ready for more clients)
  - **N per‑client sockets** (one for each active connection)
- All actual HTTP traffic (request lines, headers, bodies, and responses) travels over the **per‑client socket**—never the listening socket. Your server:
  1. **Reads** the raw bytes from the per‑client socket
  2. **Parses** the HTTP method, URL path, headers, and body
  3. **Dispatches** to the matching API handler (e.g. `GET /users`)
  4. **Writes** the HTTP response back on that same socket
- When the interaction is complete (or if `Connection: close` is used), either side initiates a graceful TCP shutdown. The OS exchanges FIN/ACK packets, the per‑client socket is closed and freed, while the listening socket remains active for new clients.

Think of the listening socket as your server’s “front door” and each per‑client socket as a private hallway for that one visitor’s conversation—HTTP endpoints (URL routes) are just the logical rooms your application takes them to once they’ve passed through that hallway.

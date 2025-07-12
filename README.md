# REAL-TIME-CHAT-SERVER

COMPANY NAME: CODETECH IT SOLUTIONS

NAME: SAMRUDHI GHANATE

Intern ID :CT12DL761

DOMAIN: BACK END DEVELOPMENT

DURATION: 11 WEEKS

MENTOR: NEELA SANTHOSH

*PROJECT DESCRIPTION*: This project is a real-time chat application built using FastAPI and WebSockets. It allows users to join chat rooms and exchange messages instantly with other users in the same room. The server manages real-time communication by handling WebSocket connections, managing chat rooms, and broadcasting messages to connected clients. The application demonstrates the use of asynchronous, bidirectional communication in Python and is suitable for any real-time application that requires low-latency messaging.

FastAPI is used as the core web framework because of its speed, simplicity, and support for asynchronous programming. WebSockets are leveraged to maintain persistent connections between clients and the server, allowing data to flow in both directions at any time without needing to refresh or make separate HTTP requests.

When a user connects, they specify a chat room to join. The server keeps track of active WebSocket connections in each room. When a message is sent by one user, it is instantly broadcasted to all users currently connected to that same room. The system ensures that messages are scoped to their respective rooms and do not leak across unrelated conversations.

The architecture follows a clear and minimalistic design. The server maintains a dictionary of rooms, where each room maps to a set of active WebSocket connections. When a user joins, their connection is added to the relevant set. When a message is received, the server loops through all the connections in the room and sends the message to each one. When a user disconnects, their WebSocket is removed from the list of active connections.

This type of application is especially useful for real-time collaborative systems such as group chats, multiplayer game lobbies, live dashboards, or notifications. It ensures that all participants in a session receive updates immediately, improving user experience and reducing the need for polling or redundant HTTP traffic.

The server is implemented with FastAPI's support for asynchronous endpoints and event handling. The WebSocket class from FastAPI handles the underlying connection protocol, and the accept, receive_text, and send_text methods manage incoming and outgoing data. The use of asynchronous functions allows the server to handle many clients concurrently without blocking, which is critical for real-time systems.

The code is clean, lightweight, and easy to extend. Developers can build additional features on top of this foundation, such as user authentication, message history, private messaging, or message persistence using a database. Currently, the application focuses on demonstrating the real-time core concept without external dependencies like databases or frontend interfaces.

The chat system is designed to be run as a standalone backend service. Any frontend, such as a JavaScript or mobile app client, can connect to it via WebSocket URLs. Messages are expected and returned in simple text format, but the design can easily be adapted to support JSON messages with metadata like timestamps, usernames, or message types.

Overall, this project provides a functional and educational example of building real-time applications in Python using FastAPI and WebSockets. It showcases key concepts in asynchronous programming, persistent connections, and event-driven architecture. Whether you're building a scalable chat platform, a collaborative tool, or learning how real-time protocols work, this project offers a strong foundation.


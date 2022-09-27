# 0x0F. Load Balancer

Implentation of Load Balancer to ensure redundancy and balance network service between the multiple servers hosting my webpage

### Files in the directory

| File name                               | Description                                                                                                               |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 0-custom_http_response_header           | Install nginx server and configure it to port 80, set the redirect_me page, 404 not found page and the X-served-By header |
| 1-install_load_balancer                 | Install and configure HAproxy on the load balancer server to serve the two web servers                                    |
| 2-puppet_custom_http_response_header.pp | Create a custom header with puppet                                                                                        |

### PS

These are tasks done as a Software Engineering student at **Alx_SE**

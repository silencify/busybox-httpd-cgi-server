# Usage

1. Navigate to `www` directory.
2. Server web server with `busybox httpd -p 8000 -fvvv -c ../config.cfg`.
3. Open browser and navigate to `localhost:8000`.
4. Browser will ask for password if configured in `config.cfg` file.

# Config file

Configuration file for server is `config.cfg`.

1. This file has server root directory defined by `H`.
2. Credentials for route is defined by `<route>:<username>:<password>`.

eg. `/home/index.html:root:abcd`. To access `/home/index.html`, root (username) and abcd (password) will be required.


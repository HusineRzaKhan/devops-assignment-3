# Dockerfile
FROM python:3.11-slim

# Set non-interactive frontend for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for Chrome and general utilities
RUN apt-get update && apt-get install -y \
    wget gnupg2 ca-certificates unzip procps fonts-liberation \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon0 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libasound2 libpangocairo-1.0-0 \
    libgtk-3-0 curl && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome (stable)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /etc/apt/trusted.gpg.d/google-linux-signing-key.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Set working directory for your tests
WORKDIR /opt/tests

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install chromedriver-binary to match installed Chrome
RUN pip install --no-cache-dir chromedriver-binary

# Copy all project files
COPY . .

# Create results directory
RUN mkdir -p results

# Set target URL environment variable
ENV TARGET_URL=https://factaccount.blog

# Set default entrypoint
ENTRYPOINT ["/opt/tests/run_tests.sh"]

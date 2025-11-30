# Dockerfile
FROM python:3.11-slim

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

# Set working directory
WORKDIR /opt/tests

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install chromedriver-binary and webdriver-manager
RUN pip install --no-cache-dir chromedriver-binary webdriver-manager

# Copy all project files
COPY . .

# Make test script executable
RUN chmod +x /opt/tests/run_tests.sh

# Create results directory
RUN mkdir -p /opt/tests/results

# Set environment variable
ENV TARGET_URL=https://factaccount.blog

# Default entrypoint
ENTRYPOINT ["/opt/tests/run_tests.sh"]

# Dockerfile
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    wget gnupg2 ca-certificates unzip procps fonts-liberation \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon0 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libasound2 libpangocairo-1.0-0 \
    libgtk-3-0 && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome (Debian/Ubuntu slim compatible)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /etc/apt/trusted.gpg.d/google-linux-signing-key.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*


# Install chromedriver that matches chrome version
RUN CHROME_VERSION=$(google-chrome --product-version | cut -d. -f1) && \
    echo "Chrome major version: $CHROME_VERSION" && \
    # find matching chromedriver — use chromedriver.storage.googleapis.com latest for major version
    CDVER=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget -q "https://chromedriver.storage.googleapis.com/${CDVER}/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip && mv chromedriver /usr/local/bin/ && chmod +x /usr/local/bin/chromedriver && rm chromedriver_linux64.zip

# Create app dir
WORKDIR /opt/tests
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p results

ENV TARGET_URL=https://factaccount.blog

ENTRYPOINT ["/opt/tests/run_tests.sh"]

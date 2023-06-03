# Use the official Node.js base image with Node.js 14
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl

# Install Node.js dependencies
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Install project dependencies
RUN npm install -g @vue/cli
RUN npm install

# Expose the port on which your frontend server runs (adjust if necessary)
EXPOSE 8080

# Start the frontend server
CMD ["npm", "run", "serve"]

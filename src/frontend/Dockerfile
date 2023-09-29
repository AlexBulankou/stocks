# Use a Node.js image
FROM node:16-slim

# Set the working directory
WORKDIR /app

# Copy the build files from the local system to the container
COPY /dist /app/dist
COPY package*.json ./

# Install serve module
RUN npm install serve

# Command to run the application
CMD ["npx", "serve", "-s", "dist", "-l", "3000"]

# Expose the port the app runs on
EXPOSE 3000

# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set the environment variable for the PostgreSQL password
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgresmaster
ENV POSTGRES_DB postgres

# Expose the default PostgreSQL port
EXPOSE 5432

# Start the PostgreSQL server when the container launches
CMD ["postgres"]
FROM phusion/baseimage:focal-1.2.0

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# TODO: Complete

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

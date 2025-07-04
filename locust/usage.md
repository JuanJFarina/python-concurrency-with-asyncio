## Usage

In order to use **locust** you can simply run:

```
locust -f path/to/file.py
```

If you are running in a not-Windows OS, or in WSL, you can use --processes:

```
locust --processes 4 -f path/to/file.py
```

Otherwise you can run the load_test.py in the following manner:

```
python load_test.py path/to/file.py
```

A UI will be available at your localhost in port 8089 which will allow you to 
run load tests.
To download and directly execute the `install_sman.sh` script from the provided URL in one command, you can use `wget` to fetch the script and then pipe it directly into `sudo` to execute it. Here's how you can do it:

```bash
wget -O - https://github.com/sabbir28/S_man/raw/main/build_excutable/linux/install_sman.sh | sudo bash
```

### Explanation:

- **`wget -O - URL`**: Downloads the script from the specified URL (`-O -` directs `wget` to output to stdout).
  
- **`|`**: Pipes the downloaded script directly into the next command.
  
- **`sudo bash`**: Runs the downloaded script with root privileges (`sudo`) using the `bash` interpreter.

### Important Note:

Running scripts directly from the internet, especially with `sudo`, can pose security risks. Ensure you trust the source before executing such commands. In this case, it assumes you trust the script provided by `https://github.com/sabbir28`.

Always review scripts obtained from the internet before executing them, especially with root privileges. If possible, download the script and inspect its contents before running it.

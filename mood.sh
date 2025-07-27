#!/bin/bash

mood=$1

case "$mood" in
  sad)
    echo "😢 Bash says: It's okay to be sad. Here's a virtual hug 🤗"
    echo "Remember: echo \":(\" > sadness.txt is still valid 🐧"
    ;;
  happy)
    echo "😄 Bash says: That's great! Spread those good vibes like 'chmod +x joy.sh'"
    ;;
  bored)
    echo "😐 Bash says: Why not run 'cmatrix' or make a useless script for fun?"
    ;;
  angry)
    echo "😠 Bash says: Don't rm -rf the world. Take a deep breath instead 🧘"
    ;;
  confused)
    echo "🤔 Bash says: Even 'man man' is confusing sometimes."
    ;;
  lonely)
    echo "😞 Bash says: You're never alone in the terminal. Type 'cowsay hello'."
    ;;
  tired)
    echo "🥱 Bash says: Try 'sleep 8h && wakeup.sh' – you deserve rest!"
    ;;
  *)
    echo "Usage: ./mood.sh [sad|happy|bored|angry|confused|lonely|tired]"
    ;;
esac

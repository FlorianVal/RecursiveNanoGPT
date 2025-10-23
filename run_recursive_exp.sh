#!/usr/bin/env bash
mkdir -p logs
for cfg in config/Recursive/*.py; do
  base=$(basename "$cfg" .py)
  echo "Launching $cfg -> out/logs/$base.out ..."
  python3 train.py "$cfg" > "out/logs/$base.out" 2>&1 &
done
wait
echo "✅ All experiments finished."
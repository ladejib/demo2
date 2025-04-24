      sh -c 'echo "Waiting for app to be healthy..." &&
      DATE=$(date +%Y%m%d_%H%M%S) &&
      echo "Using timestamp: $DATE" &&
      pytest tests/ --disable-warnings --tb=short --maxfail=3 \
        --html=/results/test_report_${DATE}.html --self-contained-html \
        | tee /results/test_log_${DATE}.txt'

PYTHONPATH="${PYTHONPATH}:/opt/google/appengine/"
sudo /root/.local/bin/nosetests-2.7  --with-gae --gae-lib-root=/opt/google/appengine

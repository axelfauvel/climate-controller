How to
===

Setup
-----
refer to [this doc](../setup.md)


API call examples
---

```bash
curl -k -X PUT -H "Content-Type: application/json" -d '{"ac_mode":"heat", "temperature": "20", "fan": "auto"}' ${RPI_URL}/v1/temperature

curl -k -X PUT ${RPI_URL}/v1/power/poweroff
```

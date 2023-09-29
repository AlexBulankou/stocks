# stocks


## Build and redeploy frontend
```
# try it
npm run build

# package and deploy
docker build -t bulankou/stocks-fe:latest .
docker login
docker push bulankou/stocks-fe:latest
kubectl rollout restart deployment/react-deployment
```

#!/bin/bash
echo "Setting up database resources..."

# Deploy database
kubectl apply -f ../../k8s/deployments/postgres-deployment.yaml
kubectl apply -f ../../k8s/deployments/redis-deployment.yaml

# Wait for postgres to be ready
echo "Waiting for PostgreSQL to be ready..."
ready=false
attempts=0
max_attempts=30

while [ "$ready" = false ] && [ $attempts -lt $max_attempts ]; do
    ((attempts++))
    echo "Attempt $attempts of $max_attempts..."
    
    podStatus=$(kubectl get pods -l app=postgres -o jsonpath="{.items[0].status.phase}" 2>/dev/null)
    
    if [ "$podStatus" = "Running" ]; then
        # Check if PostgreSQL is accepting connections
        pod_name=$(kubectl get pods -l app=postgres -o jsonpath="{.items[0].metadata.name}")
        if kubectl exec "$pod_name" -- pg_isready -h localhost > /dev/null 2>&1; then
            ready=true
            echo "PostgreSQL is ready!"
        else
            echo "PostgreSQL pod is running but not yet accepting connections..."
            sleep 5
        fi
    else
        echo "Waiting for PostgreSQL pod to be in Running state (current: $podStatus)..."
        sleep 5
    fi
done

if [ "$ready" = false ]; then
    echo "Warning: PostgreSQL did not become ready in the expected time."
    exit 1
fi
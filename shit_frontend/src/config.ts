// src/config/index.ts
interface AppConfig {
    apiBaseUrl: string;
    wsBaseUrl: string;
    sseBaseUrl: string;
    environment: 'development' | 'production' | 'test';
  }
  
  // Get environment variables or use defaults
  const getConfig = (): AppConfig => {
    // For Create React App
    const env = process.env.REACT_APP_ENV || process.env.NODE_ENV || 'development';
    
    // For local development with Minikube
    const devConfig: AppConfig = {
      apiBaseUrl: process.env.REACT_APP_API_BASE_URL || 'http://trading.local/api',
      wsBaseUrl: process.env.REACT_APP_WS_BASE_URL || 'ws://trading.local/ws',
      sseBaseUrl: process.env.REACT_APP_SSE_BASE_URL || 'http://trading.local/stream',
      environment: 'development'
    };
    
    // Production configuration (using AWS)
    const prodConfig: AppConfig = {
      apiBaseUrl: process.env.REACT_APP_API_BASE_URL || 'https://api.your-trading-domain.com/api',
      wsBaseUrl: process.env.REACT_APP_WS_BASE_URL || 'wss://api.your-trading-domain.com/ws',
      sseBaseUrl: process.env.REACT_APP_SSE_BASE_URL || 'https://api.your-trading-domain.com/stream',
      environment: 'production'
    };
    
    // Test configuration
    const testConfig: AppConfig = {
      apiBaseUrl: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8080/api',
      wsBaseUrl: process.env.REACT_APP_WS_BASE_URL || 'ws://localhost:8080/ws',
      sseBaseUrl: process.env.REACT_APP_SSE_BASE_URL || 'http://localhost:8080/stream',
      environment: 'test'
    };
    
    // Select config based on environment
    switch(env) {
      case 'production':
        return prodConfig;
      case 'test':
        return testConfig;
      default:
        return devConfig;
    }
  };
  
  // Export configuration
  export const config = getConfig();


console.log('Configuration loaded:', {
  apiBaseUrl: config.apiBaseUrl,
  wsBaseUrl: config.wsBaseUrl,
  sseBaseUrl: config.sseBaseUrl,
  environment: config.environment,
});
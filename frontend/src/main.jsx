import React from 'react';
import ReactDOM from 'react-dom/client'; // Import from 'react-dom/client' for modern rendering
import './main.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

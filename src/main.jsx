"use client";
import React from 'react';
import ReactDOM from 'react-dom/client';
import AudicoQuoteWidget from './widget.jsx';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AudicoQuoteWidget />
  </React.StrictMode>
);

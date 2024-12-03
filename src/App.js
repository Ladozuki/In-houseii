import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import DocumentUpload from './components/DocumentUpload';
import DocumentSearch from './components/DocumentSearch';
import ShipmentList from './components/ShipmentList';
import Dashboard from './components/Dashboard/Dashboard';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
         <h1>Documentation System</h1>
        <nav className="nav-links">
          <Link to="/upload" className="App-link">Upload Documents</Link>
          <Link to="/search" className="App-link">Search Documents</Link>
          <Link to="/shipments" className="App-link">View Shipments</Link>
        </nav>
        </header>
        <main className="main-container">
          <Routes>
            <Route path="/upload" element={<DocumentUpload />} />
            <Route path="/search" element={<DocumentSearch />} />
            <Route path="/shipments" element={<ShipmentList />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;


<Route path = "dashboard" element = {<Dashboard/>} />

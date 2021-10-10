import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Home from './pages/home/Home';
import QRgen from './pages/generator/QRgenerator';
import QRscan from './pages/scanner/QRscanner';

function App() {
  return (
    <div className='App'>
      <div className='App-header'>
        <Router>
          <div className='content'>
            <Switch>
              <Route exact path='/'>
                <Home />
              </Route>
              <Route path='/qr_generator'>
                <QRgen />
              </Route>
              <Route path='/qr_scanner'>
                <QRscan />
              </Route>
            </Switch>
          </div>
        </Router>
      </div>
    </div>
  );
}

export default App;

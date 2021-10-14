import React, { useState } from 'react';
import { Fab, TextField, Typography, Grid } from '@material-ui/core';
import { ArrowBack, GetApp } from '@material-ui/icons';
import { Link } from 'react-router-dom';
import QRcode from 'qrcode.react';

import './generator.css';

function QRgenerator() {
  const [qr, setQr] = useState('');
  const handleChange = (event) => {
    setQr(event.target.value);
  };
  const downloadQR = () => {
    const canvas = document.getElementById('myqr');
    const pngUrl = canvas
      .toDataURL('image/png')
      .replace('image/png', 'image/octet-stream');
    let downloadLink = document.createElement('a');
    downloadLink.href = pngUrl;
    let x = qr.toLowerCase();
    downloadLink.download = x + '.png';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  };

  return (
    <div className='center'>
      <Grid container spacing={2}>
        <Grid item xs>
          <Link to='/'>
            <Fab className='bt' style={{ marginRight: 10 }} color='primary'>
              <ArrowBack />
            </Fab>
          </Link>
          <Typography className='generator' variant='h2'>
            QR GENERATOR
          </Typography>
        </Grid>

        <Grid item xs>
          <div style={{ marginTop: 30 }} className='textfield'>
            <TextField
              onChange={handleChange}
              style={{ width: 320 }}
              value={qr}
              label='QR content'
              size='large'
              variant='outlined'
            />
          </div>

          <div>
            {qr ? (
              <QRcode id='myqr' value={qr} size={320} includeMargin={true} />
            ) : (
              <p>No QR code preview</p>
            )}
          </div>
          <div>
            {qr ? (
              <Grid item xs>
                <Fab onClick={downloadQR} color='primary' className='bt'>
                  <GetApp />
                </Fab>
              </Grid>
            ) : (
              ''
            )}
          </div>
        </Grid>
      </Grid>
    </div>
  );
}

export default QRgenerator;

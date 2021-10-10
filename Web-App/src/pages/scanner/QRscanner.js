import React, { useState } from 'react';
import { Fab, TextareaAutosize, Grid, Typography } from '@material-ui/core';
import { ArrowBack } from '@material-ui/icons';
import { Link } from 'react-router-dom';
import QrScan from 'react-qr-reader';
// import Speech from 'react-speech';
import { useSpeechSynthesis } from 'react-speech-kit';

import './scanner.css';

function QRscanner() {
  const [qrscan, setQrscan] = useState('');
  const handleScan = (data) => {
    if (data) {
      setQrscan(data);
    }
  };
  const handleError = (err) => {
    console.error(err);
  };
  const { speak } = useSpeechSynthesis();

  return (
    <div className='center'>
      <Grid container spacing={2}>
        <Grid item xs>
          <Link to='/'>
            <Fab style={{ marginRight: 10 }} color='primary' className='bt'>
              <ArrowBack />
            </Fab>
          </Link>
          <Typography className='generator' variant='h2'>
            QR SCANNER
          </Typography>
        </Grid>

        <Grid item xs>
          <center>
            <div style={{ marginTop: 30 }}>
              <QrScan
                delay={300}
                onError={handleError}
                onScan={handleScan}
                style={{ height: 240, width: 320 }}
                // onChange={() => speak({ text: qrscan })}
              />
            </div>
          </center>

          <TextareaAutosize
            onChange={() => speak({ text: qrscan })}
            style={{ fontSize: 18, width: 320, height: 100, marginTop: 100 }}
            rowsMax={4}
            defaultValue={qrscan}
            value={qrscan}
          />
        </Grid>
      </Grid>

      {/* <button onClick={() => speak({ text: qrscan })}>Speak</button> */}

      {/* <Speech text={qrscan} /> */}
    </div>
  );
}

export default QRscanner;

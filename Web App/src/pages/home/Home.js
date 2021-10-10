import { Grid, Button, Typography } from '@material-ui/core';
import Icon from '@mdi/react';
import { mdiQrcode, mdiQrcodeScan } from '@mdi/js';
import { Link } from 'react-router-dom';

import './home.css';

function Home() {
  return (
    <div className='center'>
      <Typography className='heading' variant='h1' m={20}>
        LAB EYES
      </Typography>

      <Grid container spacing={2}>
        <Grid item xs>
          <Link to='/qr_generator'>
            <Button className='bt' variant='contained' size='large'>
              <Icon
                style={{ padding: 10 }}
                path={mdiQrcode}
                title='QR Generator'
                size={10}
                color='white'
              />
            </Button>
          </Link>
          <Typography className='sub-heading' variant='h3' m={20}>
            QR GENERATOR
          </Typography>
        </Grid>
        <Grid item xs>
          <Link to='/qr_scanner'>
            <Button
              className='bt'
              variant='contained'
              size='large'
              color='primary'
            >
              <Icon
                style={{ padding: 10 }}
                path={mdiQrcodeScan}
                title='QR Scanner'
                size={10}
                color='white'
              />
            </Button>
          </Link>
          <Typography className='sub-heading' variant='h3' m={20}>
            QR SCANNER
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
}

export default Home;

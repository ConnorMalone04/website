import { ChangeEvent, useState } from 'react';
import axios from 'axios';

export default function Home() {
  return (
      <div>
        {axios.get('/app')}
      </div>
  );
}

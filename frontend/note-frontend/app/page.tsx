import Image from "next/image";
import { text } from "stream/consumers";

export default function Home() {
  return (
    <div>
      <h1>
        <p style={{ color: 'blue',
          fontSize: '24px',
          textAlign: 'center',
          marginTop: '20px'
         }}>Welcome to Acme</p>
      </h1>
    </div>
  );
}

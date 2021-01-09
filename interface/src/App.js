import React, { useState, useEffect } from "react";
import TextField, { HelperText, Input } from '@material/react-text-field';
import MaterialIcon from '@material/react-material-icon';
import Button from '@material/react-button';
import Card, {
  CardPrimaryContent,
  CardMedia,
  CardActions,
  CardActionButtons,
  CardActionIcons
} from "@material/react-card";

import './App.scss';

function App() {

  const [mail, setMail] = useState("");
  const [result, setResult] = useState("");

  async function processEmail() {
    try {
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: mail })
      })
      const json = await response.json();
      setResult(json.prediction ? "SPAM" : "Valide")
    } catch (error) {

    }
  }

  return (
    <div className="App">

      <Card className="App-Card">
        <h2>Python for data analysis</h2>
        <div
          className="Email-Input-Container"
        >
          <TextField
            label='Email'
            className="Email-Input"
            outlined={true}
            textarea={true}
            helperText={<HelperText>Insérer un email pour vérifier s'il s'agit d'un SPAM</HelperText>}
            onTrailingIconSelect={() => { setMail(''); setResult("") }}
            trailingIcon={<MaterialIcon role="button" icon="delete" />}
          ><Input
              value={mail}
              onChange={(e) => setMail(e.currentTarget.value)} />
          </TextField>
        </div>
        <CardActions>
          <CardActionButtons>
            <Button
              outlined={true}
              onClick={processEmail}>
              Tester cet email
      </Button>
          </CardActionButtons>

          <CardActionIcons>
            <i>{result}</i>
          </CardActionIcons>
        </CardActions>






      </Card>
    </div >
  );
}

export default App;

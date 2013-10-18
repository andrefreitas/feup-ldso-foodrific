package feup.mieic.foodrific;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.view.Window;
import android.widget.EditText;
import android.widget.Toast;

public class LoginActivity extends Activity {
	
	public final static String EXTRA_USERNAME = "feup.mieic.foodrific.USERNAME";
	public final static String EXTRA_PASSWORD = "feup.mieic.foodrific.PASSWORD";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.activity_login);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.login, menu);
		return true;
	}
	
	public void login(View view){
		
		EditText usernameEditText = (EditText) findViewById(R.id.UsernameEditText);
		EditText passwordEditText = (EditText) findViewById(R.id.PasswordEditText);
		
		String username = usernameEditText.getText().toString();
		String password = passwordEditText.getText().toString();	
		
		if(!validateUsername(username)){
			Toast.makeText(getApplicationContext(), "Invalid Email", Toast.LENGTH_LONG).show();
			
		}else if(password.isEmpty()){
			Toast.makeText(getApplicationContext(), "Empty Password", Toast.LENGTH_LONG).show();			
		}
		else{
			//TODO validar login com servidor
			
			//se login valido entao:
			callFeedIntent(username, password);
		}
	}

	private boolean validateUsername(String username) {
		if(username == null){
			return false;
		} else {
			return android.util.Patterns.EMAIL_ADDRESS.matcher(username).matches();
		}
	}

	private void callFeedIntent(String username, String password) {
		Intent feedIntent = new Intent(this, FeedActivity.class);
		
		feedIntent.putExtra(EXTRA_USERNAME, username);
		feedIntent.putExtra(EXTRA_PASSWORD, password);
		
		startActivity(feedIntent);
	}
}

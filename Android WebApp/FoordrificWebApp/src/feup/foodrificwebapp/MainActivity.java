package feup.foodrificwebapp;

import feup.foodrificwebapp.R;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.net.Uri;
import android.os.Bundle;
import android.os.SystemClock;
import android.text.AndroidCharacter;
import android.view.KeyEvent;
import android.view.Window;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;
import android.app.Activity;
import android.app.AlertDialog;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;

public class MainActivity extends Activity {

	private WebView foodrificwebView;

	public void ringtone(){
		try {
			Uri notification = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
			Ringtone r = RingtoneManager.getRingtone(getApplicationContext(), notification);
			r.play();
		} catch (Exception e) {}
	}
	private boolean isNetworkConnected() {
		ConnectivityManager cm = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
		NetworkInfo ni = cm.getActiveNetworkInfo();
		if (ni == null) {
			// There are no active networks.
			return false;
		} else
			return true;
	}

	public void onCreate(Bundle savedInstanceState) {
		ConnectivityManager cm =
				(ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);

		NetworkInfo activeNetwork = cm.getActiveNetworkInfo();

		boolean connectionDone = isNetworkConnected();

		if(connectionDone)
			System.out.println("Connected");
		else			
		{
			ringtone();
			Toast.makeText(getApplicationContext(), "No Internet!", Toast.LENGTH_SHORT).show();
			NotificationManager nm=(NotificationManager)getSystemService(Context.NOTIFICATION_SERVICE);
			Notification notification=new Notification(android.R.drawable.stat_notify_more, "IMPORTANTE", System.currentTimeMillis());
			Context context=MainActivity.this;
			CharSequence title="Falha de ligação";
			CharSequence detail="Por favor ligue a Internet";
			Intent intent=new Intent(context,MainActivity.class);
			PendingIntent  pending=PendingIntent.getActivity(context, 0, intent, 0);
			notification.setLatestEventInfo(context, title, detail, pending);
			nm.notify(0, notification);
			SystemClock.sleep(600);
			android.os.Process.killProcess(android.os.Process.myPid());
			System.exit(1);
		}

		boolean isConnected = activeNetwork != null &&
				activeNetwork.isConnectedOrConnecting();
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.activity_main);

		foodrificwebView = (WebView) findViewById(R.id.webView);


		if (isConnected) {
			foodrificwebView.getSettings().setJavaScriptEnabled(true);
			foodrificwebView.setWebViewClient(new Callback());
			foodrificwebView.loadUrl("http://www.foodrific.appspot.com");
		}
		
		foodrificwebView.setWebViewClient(new WebViewClient() {
			public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
				foodrificwebView.loadUrl("file:///android_asset/myerrorpage.html");

			}
		});

	}


	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		// Check if the key event was the Back button and if there's history
		if ((keyCode == KeyEvent.KEYCODE_BACK) && foodrificwebView.canGoBack()) {
			foodrificwebView.goBack();
			return true;
		}
		else {
			Intent i = new Intent(getApplicationContext(), MainActivity.class);
			startActivity(i);
		}
		// If it wasn't the Back key or there's no web page history, bubble up to the default
		// system behavior (probably exit the activity)
		return super.onKeyDown(keyCode, event);
	}

	private class Callback extends WebViewClient{  

		@Override
		public boolean shouldOverrideUrlLoading(WebView view, String url) {
			if (Uri.parse(url).getHost().equals("www.foodrific.appspot.com")) {
				// This is my web site, so do not override; let my WebView load the page
				return false;
			}
			// Otherwise, the link is not for a page on my site, so launch another Activity that handles URLs
			Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
			startActivity(intent);
			return true;
		}

	}

}

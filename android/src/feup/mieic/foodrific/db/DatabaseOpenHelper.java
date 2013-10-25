package feup.mieic.foodrific.db;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseOpenHelper extends SQLiteOpenHelper {
	
	private static final int DATABASE_VERSION = 2;
    private static final String DICTIONARY_TABLE_NAME = "userlogin";
    private static final String KEY_USERNAME = "username";
    private static final String KEY_PASS = "password";
    private static final String DICTIONARY_TABLE_CREATE =
                "CREATE TABLE " + DICTIONARY_TABLE_NAME + " (" +
                KEY_USERNAME + " TEXT, " +
                KEY_PASS + " TEXT);";
	private static final String DATABASE_NAME = "foodrific.db";

    public DatabaseOpenHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

	@Override
	public void onCreate(SQLiteDatabase db) {
		db.execSQL(DICTIONARY_TABLE_CREATE);
	}

	@Override
	public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {}

}

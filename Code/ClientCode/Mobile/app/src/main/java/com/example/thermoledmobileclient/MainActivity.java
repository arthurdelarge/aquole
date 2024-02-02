package com.example.thermoledmobileclient;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;

import android.app.Activity;
import android.content.Context;
import android.os.AsyncTask;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.example.thermoledmobileclient.data.model.LoggedInUser;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.lang.ref.WeakReference;
import java.util.concurrent.TimeUnit;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.examples.iotservice.IoTServiceGrpc;
import io.grpc.examples.iotservice.AccelerationReply;
import io.grpc.examples.iotservice.AccelerationRequest;


public class MainActivity extends AppCompatActivity {
    private TextView accelerationResultText;
    private String host;
    private int port;
    private int key;
    private Button getAccelerationButton;

    private LoggedInUser user;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        LoginViewModel vm = new ViewModelProvider(this, new LoginViewModelFactory())
                .get(LoginViewModel.class);
        user = vm.getLoggedInUser();
        accelerationResultText = (TextView) findViewById(R.id.textViewAcceleration);
        host = user.getUserHost();
        port = user.getUserPort();
        key = user.getUserId();
//        hostEdit = (EditText) findViewById(R.id.host);
//        portEdit = (EditText) findViewById(R.id.port);
        getAccelerationButton = (Button) findViewById(R.id.getTempButton);

    }

    public void sendAccelerationRequest(View view) {
//        ((InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE))
//                .hideSoftInputFromWindow(hostEdit.getWindowToken(), 0);
        getAccelerationButton.setEnabled(false);
        accelerationResultText.setText("");
        Integer iport = new Integer(port);
        Integer ikey = new Integer(key);
        new GrpcTask(this).execute(host,iport.toString(), ikey.toString());
    }

    private static class GrpcTask extends AsyncTask<String, Void, String> {
        private final WeakReference<Activity> activityReference;
        private ManagedChannel channel;


        private GrpcTask(Activity activity) {
            this.activityReference = new WeakReference<Activity>(activity);
        }

        @Override
        protected String doInBackground(String... params) {

            String host = params[0];
            String portStr = params[1];
            String keyStr = params[2];
            int port = TextUtils.isEmpty(portStr) ? 0 : Integer.parseInt(portStr);
            int key = TextUtils.isEmpty(keyStr) ? 0 : Integer.parseInt(keyStr);

            try {
                channel = ManagedChannelBuilder.forAddress(host, port).usePlaintext().build();
                IoTServiceGrpc.IoTServiceBlockingStub stub = IoTServiceGrpc.newBlockingStub(channel);
                AccelerationRequest request = AccelerationRequest.newBuilder().setKey(key).build();
                AccelerationReply reply = stub.sayAcceleration(request);
                if(reply.getStatus().equals("OK"))
                    return reply.getAcceleration();
                throw new Exception(reply.getStatus());
            } catch (Exception e) {
                StringWriter sw = new StringWriter();
                PrintWriter pw = new PrintWriter(sw);
                e.printStackTrace(pw);
                pw.flush();
                return String.format("Failed... : %n%s", sw);
            }
        }

        @Override
        protected void onPostExecute(String result) {
            try {
                channel.shutdown().awaitTermination(1, TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            Activity activity = activityReference.get();
            if (activity == null) {
                return;
            }
            TextView accelerationResultText = (TextView) activity.findViewById(R.id.textViewAcceleration);
            Button getAccelerationButton = (Button) activity.findViewById(R.id.getTempButton);
            accelerationResultText.setText(result);
            getAccelerationButton.setEnabled(true);
        }
    }

    private static class GrpcTask2 extends AsyncTask<String, Void, String> {
        private final WeakReference<Activity> activityReference;
        private ManagedChannel channel;


        private GrpcTask2(Activity activity) {
            this.activityReference = new WeakReference<Activity>(activity);
        }

        @Override
        protected String doInBackground(String... params) {

            String host = params[0];
            String portStr = params[1];
            String keyStr = params[2];
            int port = TextUtils.isEmpty(portStr) ? 0 : Integer.parseInt(portStr);
            int key = TextUtils.isEmpty(keyStr) ? 0 : Integer.parseInt(keyStr);
            try {
                channel = ManagedChannelBuilder.forAddress(host, port).usePlaintext().build();
                IoTServiceGrpc.IoTServiceBlockingStub stub = IoTServiceGrpc.newBlockingStub(channel);
            } catch (Exception e) {
                StringWriter sw = new StringWriter();
                PrintWriter pw = new PrintWriter(sw);
                e.printStackTrace(pw);
                pw.flush();
                return String.format("Failed... : %n%s", sw);
            }
        }

        @Override
        protected void onPostExecute(String result) {
            try {
                channel.shutdown().awaitTermination(1, TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            Activity activity = activityReference.get();
            if (activity == null) {
                return;
            }
        }
    }
}

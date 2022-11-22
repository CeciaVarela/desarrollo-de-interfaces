package com.example.myothercatalog;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;

public class AnimalViewHolder extends RecyclerView.ViewHolder{
    private final TextView textView;
    private final ImageView imageView;

    public AnimalViewHolder(@NonNull View itemView){
        super(itemView);
        textView = itemView.findViewById(R.id.animal_name_text_view);
        imageView = itemView.findViewById(R.id.animal_image_view);
    }

    public void showData(AnimalData data, Activity activity){
        textView.setText(data.getName());
        cancelPreviousImageDownloadIfAny();
        loadImage(data.getImageUrl(), activity);
    }

    private void cancelPreviousImageDownloadIfAny(){}

    private void loadImage(String imageUrl, Activity activity) {

        String targetURL = imageUrl;
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Bitmap image = getBitmapFromURL(targetURL);
                activity.runOnUiThread(new Runnable(){
                    @Override
                    public void run(){
                        imageView.setImageBitmap(image);
                    }
                });
            }
        });
        thread.start();
    }

    private Bitmap getBitmapFromURL(String urlString) {
        try{
            URL url = new URL(urlString);
            URLConnection connection = url.openConnection();
            connection.connect();
            InputStream input = connection.getInputStream();
            Bitmap resultBitmap = BitmapFactory.decodeStream(input);
            return resultBitmap;
        } catch (IOException e){
            e.printStackTrace();
            return null;
        }
    }
}

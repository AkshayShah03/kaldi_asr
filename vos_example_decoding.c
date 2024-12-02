#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>
#include <portaudio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include "kaldi_recognizer.h" // Assuming you have a header file for Kaldi recognizer

#define SAMPLE_RATE 16000
#define FRAME_SIZE 256

static int callback(const void *inputBuffer, void *outputBuffer,
                    unsigned long framesPerBuffer,
                    const PaStreamCallbackTimeInfo *timeInfo,
                    PaStreamCallbackFlags statusFlags,
                    void *userData) {
    // Assuming you have a function to process audio data in Kaldi
    // kaldi_process_audio(inputBuffer, framesPerBuffer);
    return paContinue;
}

int main(int argc, char *argv[]) {
    PaStream *stream;
    PaError err;

    // Initialize Kaldi recognizer
    if (!kaldi_recognizer_initialize("/path/to/model")) {
        printf("Failed to initialize Kaldi recognizer.\n");
        return 1;
    }

    // Initialize PortAudio
    err = Pa_Initialize();
    if (err != paNoError) {
        printf("PortAudio error: %s\n", Pa_GetErrorText(err));
        return 1;
    }

    // Open the audio stream
    err = Pa_OpenDefaultStream(&stream, 1, 0, paInt16, SAMPLE_RATE, FRAME_SIZE, callback, NULL);
    if (err != paNoError) {
        printf("PortAudio error: %s\n", Pa_GetErrorText(err));
        return 1;
    }

    // Start the stream
    err = Pa_StartStream(stream);
    if (err != paNoError) {
        printf("PortAudio error: %s\n", Pa_GetErrorText(err));
        return 1;
    }

    printf("Listening...\n");

    // Wait for Enter key to stop
    getchar();

    // Stop and close the stream
    err = Pa_StopStream(stream);
    if (err != paNoError) {
        printf("PortAudio error: %s\n", Pa_GetErrorText(err));
        return 1;
    }

    err = Pa_CloseStream(stream);
    if (err != paNoError) {
        printf("PortAudio error: %s\n", Pa_GetErrorText(err));
        return 1;
    }

    // Terminate PortAudio
    err = Pa_Terminate();
    if (err != paNoError) {
        printf("PortAudio error: %s\n", Pa_GetErrorText(err));
        return 1;
    }

    // Finalize Kaldi recognizer
    kaldi_recognizer_finalize();

    return 0;
}


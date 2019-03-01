public class VoiceAnalysis {

    private double[] voiceSignal;

    public VoiceAnalysis(double[] voiceSignal){
        this.voiceSignal = voiceSignal;
    }

    public void getFeatures(){
//        return the features, i.e shimmer, jitter, etc
    }

    //e.g.
    private double getAbsoluteShimmer(){
        return 0.1;
    }

    //e.g.
    private double getJitter(){
        return 0.1;
    }

    //etc
}

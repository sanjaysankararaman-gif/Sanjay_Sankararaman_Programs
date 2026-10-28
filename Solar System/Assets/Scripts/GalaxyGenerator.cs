using UnityEngine;

public class GalaxyGenerator : MonoBehaviour
{
    public int starCount = 12000;
    public int armCount = 2;            // the Milky Way's two major arms
    public ParticleSystem ps;
    public float galaxyRadius = 50f;
    public float windings = 1.2f;       // full turns each arm makes from core to edge
    public float armSpread = 14f;       // degrees of scatter around each arm (bigger = fuzzier)
    public float bulgeFraction = 0.2f;  // share of stars packed into the central bulge
    public float bulgeRadius = 9f;
    public float discFraction = 0.2f;   // faint stars filling the space between arms
    public float diskThickness = 1.5f;
    public float rotationSpeed = 1.5f;  // slow spin, degrees per second

    // Bell-curve random number (Box-Muller): most values near 0, few far out
    static float Gaussian()
    {
        float u1 = 1f - Random.value;
        float u2 = Random.value;
        return Mathf.Sqrt(-2f * Mathf.Log(u1)) * Mathf.Cos(2f * Mathf.PI * u2);
    }

    void Start()
    {
       if (ps == null) ps = GetComponent<ParticleSystem>();
        ParticleSystem.Particle[] particles = new ParticleSystem.Particle[starCount];

        Color coreColor = new Color(1f, 0.85f, 0.55f);
        Color armColor  = new Color(0.65f, 0.8f, 1f);
        Color hiiColor  = new Color(1f, 0.55f, 0.75f);  // pink star-forming regions

        for (int i = 0; i < starCount; i++)
        {
            float pick = Random.value;
            Vector3 pos;
            Color col;
            float size;

            if (pick < bulgeFraction)
            {
                // Central bulge: a round, squashed blob of warm stars
                pos = new Vector3(Gaussian(), Gaussian() * 0.6f, Gaussian()) * (bulgeRadius * 0.45f);
                col = Color.Lerp(coreColor, Color.white, Random.value * 0.4f);
                size = Random.Range(0.25f, 0.6f);
            }
            else if (pick < bulgeFraction + discFraction)
            {
                // Faint background stars between the arms
                float d = galaxyRadius * Mathf.Sqrt(Random.value);
                float a = Random.value * Mathf.PI * 2f;
                float y = Gaussian() * diskThickness * (1f - d / galaxyRadius) * 0.4f;
                pos = new Vector3(Mathf.Cos(a) * d, y, Mathf.Sin(a) * d);
                Color c = Color.Lerp(coreColor, armColor, d / galaxyRadius);
                col = new Color(c.r, c.g, c.b, 0.5f);
                size = Random.Range(0.1f, 0.25f);
            }
            else
            {
                // Spiral arm stars
                float t = Mathf.Pow(Random.value, 1.3f);   // more stars near the center
                float d = Mathf.Lerp(bulgeRadius * 0.4f, galaxyRadius, t);
                int arm = Random.Range(0, armCount);
                float angle = (360f / armCount) * arm + (d / galaxyRadius) * windings * 360f;
                angle += Gaussian() * armSpread;

                float rad = angle * Mathf.Deg2Rad;
                float y = Gaussian() * diskThickness * (1f - t * 0.7f) * 0.4f;
                pos = new Vector3(Mathf.Cos(rad) * d, y, Mathf.Sin(rad) * d);

                float blue = Mathf.SmoothStep(0f, 1f, t * 1.3f);
                col = Color.Lerp(coreColor, armColor, blue);
                if (Random.value < 0.04f) col = hiiColor;
                size = Random.Range(0.12f, 0.35f);
            }

            particles[i].position = pos;
            particles[i].startColor = col;
            particles[i].startSize = size;
            particles[i].startLifetime = 1000000f;
            particles[i].remainingLifetime = 1000000f;
        }

        ps.SetParticles(particles, particles.Length);
    }

    void Update()
    {
        ps.transform.Rotate(Vector3.up, rotationSpeed * Time.deltaTime, Space.Self);

    }
}
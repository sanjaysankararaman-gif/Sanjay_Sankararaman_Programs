using UnityEngine;

public class AsteroidBelt : MonoBehaviour
{
    public GameObject[] asteroidPrefabs; // now an array, drag multiple prefabs in
    public int asteroidCount = 500;
    public float innerRadius = 12f;
    public float outerRadius = 15f;
    public float minScale = 0.05f;
    public float maxScale = 0.2f;
    public float beltHeight = 0.5f;

    void Start()
    {
        for (int i = 0; i < asteroidCount; i++)
        {
            float angle = Random.Range(0f, Mathf.PI * 2f);
            float radius = Random.Range(innerRadius, outerRadius);
            float x = Mathf.Cos(angle) * radius;
            float z = Mathf.Sin(angle) * radius;
            float y = Random.Range(-beltHeight, beltHeight);

            // pick a random prefab from the array instead of always using one
            GameObject prefabToSpawn = asteroidPrefabs[Random.Range(0, asteroidPrefabs.Length)];

            GameObject asteroid = Instantiate(prefabToSpawn, transform);
            asteroid.transform.localPosition = new Vector3(x, y, z);

            float scale = Random.Range(minScale, maxScale);
            asteroid.transform.localScale = Vector3.one * scale;
            asteroid.transform.rotation = Random.rotation;
        }
    }
}
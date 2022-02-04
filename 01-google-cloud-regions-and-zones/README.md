# Region and Zones

## Regions

Advantages:

- High availability
- Low latency
- Global footprint
- Adhere to government regulations

## Zones

How to achieve high availability in the same region (or geographical location) ?

- Enter **Zones**.
  Each region has 3 or more **zones**.

Advantages:

- **Increased availability and fault tolerance** within same region.

> Each zone has **one or more discrete clusters**. (*A cluster is a distinct physical infrastructure that is housed in a data center.*)
>
> Zones in a region are connected through **low-latency** links.

## Examples

| Region code   | Region                            | Zones | Zones list                                                  |
| ------------- | --------------------------------- | ----- | ----------------------------------------------------------- |
| us-west1      | The Dallas, Oregon, North America | 3     | us-west1-a,<br />us-west1-b,<br />us-west1-c                |
| europe-north1 | Hamina, Finland, Europe           | 3     | europe-north1-a,<br />europe-north1-b,<br />europe-north1-c |
| asia-south1   | Mumbai, India APAC                | 3     | asia-south1-a,<br />asia-south1-b,<br />asia-south1-c       |


/*
 * Amazon Shipping API
 * The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.
 *
 * OpenAPI spec version: v2
 * Contact: swa-api-core@amazon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.shipping.v2;

import com.google.gson.annotations.SerializedName;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.Objects;

/**
 * The request schema for the directPurchaseShipment operation. When the channel type is Amazon, the shipTo address is
 * not required and will be ignored.
 */
@Schema(
        description =
                "The request schema for the directPurchaseShipment operation. When the channel type is Amazon, the shipTo address is not required and will be ignored.")
public class DirectPurchaseRequest {
    @SerializedName("shipTo")
    private Address shipTo = null;

    @SerializedName("shipFrom")
    private Address shipFrom = null;

    @SerializedName("returnTo")
    private Address returnTo = null;

    @SerializedName("packages")
    private PackageList packages = null;

    @SerializedName("channelDetails")
    private ChannelDetails channelDetails = null;

    @SerializedName("labelSpecifications")
    private RequestedDocumentSpecification labelSpecifications = null;

    public DirectPurchaseRequest shipTo(Address shipTo) {
        this.shipTo = shipTo;
        return this;
    }

    /**
     * Get shipTo
     *
     * @return shipTo
     */
    @Schema(description = "")
    public Address getShipTo() {
        return shipTo;
    }

    public void setShipTo(Address shipTo) {
        this.shipTo = shipTo;
    }

    public DirectPurchaseRequest shipFrom(Address shipFrom) {
        this.shipFrom = shipFrom;
        return this;
    }

    /**
     * Get shipFrom
     *
     * @return shipFrom
     */
    @Schema(description = "")
    public Address getShipFrom() {
        return shipFrom;
    }

    public void setShipFrom(Address shipFrom) {
        this.shipFrom = shipFrom;
    }

    public DirectPurchaseRequest returnTo(Address returnTo) {
        this.returnTo = returnTo;
        return this;
    }

    /**
     * Get returnTo
     *
     * @return returnTo
     */
    @Schema(description = "")
    public Address getReturnTo() {
        return returnTo;
    }

    public void setReturnTo(Address returnTo) {
        this.returnTo = returnTo;
    }

    public DirectPurchaseRequest packages(PackageList packages) {
        this.packages = packages;
        return this;
    }

    /**
     * Get packages
     *
     * @return packages
     */
    @Schema(description = "")
    public PackageList getPackages() {
        return packages;
    }

    public void setPackages(PackageList packages) {
        this.packages = packages;
    }

    public DirectPurchaseRequest channelDetails(ChannelDetails channelDetails) {
        this.channelDetails = channelDetails;
        return this;
    }

    /**
     * Get channelDetails
     *
     * @return channelDetails
     */
    @Schema(required = true, description = "")
    public ChannelDetails getChannelDetails() {
        return channelDetails;
    }

    public void setChannelDetails(ChannelDetails channelDetails) {
        this.channelDetails = channelDetails;
    }

    public DirectPurchaseRequest labelSpecifications(RequestedDocumentSpecification labelSpecifications) {
        this.labelSpecifications = labelSpecifications;
        return this;
    }

    /**
     * Get labelSpecifications
     *
     * @return labelSpecifications
     */
    @Schema(description = "")
    public RequestedDocumentSpecification getLabelSpecifications() {
        return labelSpecifications;
    }

    public void setLabelSpecifications(RequestedDocumentSpecification labelSpecifications) {
        this.labelSpecifications = labelSpecifications;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        DirectPurchaseRequest directPurchaseRequest = (DirectPurchaseRequest) o;
        return Objects.equals(this.shipTo, directPurchaseRequest.shipTo)
                && Objects.equals(this.shipFrom, directPurchaseRequest.shipFrom)
                && Objects.equals(this.returnTo, directPurchaseRequest.returnTo)
                && Objects.equals(this.packages, directPurchaseRequest.packages)
                && Objects.equals(this.channelDetails, directPurchaseRequest.channelDetails)
                && Objects.equals(this.labelSpecifications, directPurchaseRequest.labelSpecifications);
    }

    @Override
    public int hashCode() {
        return Objects.hash(shipTo, shipFrom, returnTo, packages, channelDetails, labelSpecifications);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class DirectPurchaseRequest {\n");

        sb.append("    shipTo: ").append(toIndentedString(shipTo)).append("\n");
        sb.append("    shipFrom: ").append(toIndentedString(shipFrom)).append("\n");
        sb.append("    returnTo: ").append(toIndentedString(returnTo)).append("\n");
        sb.append("    packages: ").append(toIndentedString(packages)).append("\n");
        sb.append("    channelDetails: ")
                .append(toIndentedString(channelDetails))
                .append("\n");
        sb.append("    labelSpecifications: ")
                .append(toIndentedString(labelSpecifications))
                .append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
